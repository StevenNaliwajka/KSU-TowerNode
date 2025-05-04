import subprocess
import time
from datetime import datetime, timedelta

# ---- Remote Pi Parameters ----
pi_user = "tvws"
pi_host = "192.168.1.204"  # Pi IP address
pi_password = "tvws1"
remote_pi = f"{pi_user}@{pi_host}"
remote_dir = "~/TVWSDataScraper/SDR" #Pi  containing IQ files
remote_csv_dir = "~/Documents/KSU-TowerNode/CSVOutput"  # Location to save IQ files

# ---- Local Save Path ----
local_save_dir = "/opt/TVWSDataScraper/SDR"

# ---- HackRF Settings ----
center_freq = 491_000_000
sample_rate = 20_000_000
capture_duration = 4  # seconds

# ---- Capture interval ----
interval = 29 * 60  # 29 minutes in seconds

# ---- Retry Settings ----
max_retries = 3
retry_delay = 10  # seconds

while True:
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    remote_filename = f"{remote_dir}/{timestamp}.iq"
    local_filename = f"{local_save_dir}/{timestamp}.iq"

    print(f"\n[{now}] Checking for latest soil data timestamp on {pi_host}...")

    try:
        # --- 1. Get latest soil CSV timestamp ---
        get_timestamp_cmd = (
            f"sshpass -p {pi_password} ssh -o StrictHostKeyChecking=no {remote_pi} "
            f"\"find {remote_csv_dir} -name '*.csv' -printf '%T@ %p\\n' | sort -nr | head -n1\""
        )
        output = subprocess.check_output(get_timestamp_cmd, shell=True, text=True).strip()

        if not output:
            raise ValueError("No CSV files found.")

        timestamp_sec = float(output.split()[0])
        latest_csv_time = datetime.fromtimestamp(timestamp_sec)

        # Calculate when to trigger HackRF
        target_time = latest_csv_time + timedelta(seconds=58)
        wait_seconds = (target_time - datetime.now()).total_seconds()

        if wait_seconds > 0:
            print(f"[{datetime.now()}] Waiting {wait_seconds:.2f} seconds until HackRF capture...")
            time.sleep(wait_seconds)
        else:
            print(f"[{datetime.now()}] WARNING: Timestamp already passed. Running HackRF immediately.")

    except Exception as e:
        print(f"[{datetime.now()}] ERROR: Failed to get soil timestamp: {e}")
        print(f"[{datetime.now()}] Skipping this cycle...")
        time.sleep(interval)
        continue

    # --- 2. Start remote HackRF capture ---
    print(f"[{datetime.now()}] Starting HackRF capture on {pi_host}...")

    hackrf_command = (
        f"hackrf_transfer -f {center_freq} -s {sample_rate} "
        f"-n {sample_rate * capture_duration} -r {remote_filename} "
        f"-a 0 -l 16 -g 16"
    )

    ssh_cmd = [
        "sshpass", "-p", pi_password,
        "ssh", "-o", "StrictHostKeyChecking=no",
        remote_pi,
        hackrf_command
    ]

    try:
        subprocess.run(ssh_cmd, check=True)
        print(f"[{datetime.now()}] Remote capture complete: {remote_filename}")
    except subprocess.CalledProcessError as e:
        print(f"[{datetime.now()}] ERROR: Remote HackRF capture failed: {e}")
        time.sleep(interval)
        continue

    # --- 3. Pull the file from the Pi via SCP ---
    scp_cmd = [
        "sshpass", "-p", pi_password,
        "scp", "-o", "StrictHostKeyChecking=no",
        f"{remote_pi}:{remote_filename}",
        local_filename
    ]

    success = False
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[{datetime.now()}] Attempt {attempt}: Pulling {remote_filename} via SCP...")
            subprocess.run(scp_cmd, check=True)
            success = True
            print(f"[{datetime.now()}] Transfer successful to {local_filename}")
            break
        except subprocess.CalledProcessError:
            print(f"[{datetime.now()}] SCP attempt {attempt} failed. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

    if success:
        # --- 4. Delete the remote file ---
        delete_cmd = [
            "sshpass", "-p", pi_password,
            "ssh", "-o", "StrictHostKeyChecking=no",
            remote_pi,
            f"rm -f {remote_filename}"
        ]
        try:
            subprocess.run(delete_cmd, check=True)
            print(f"[{datetime.now()}] Deleted remote file {remote_filename}.")
        except subprocess.CalledProcessError as e:
            print(f"[{datetime.now()}] WARNING: Could not delete remote file: {e}")
    else:
        print(f"[{datetime.now()}] ERROR: Failed to retrieve {remote_filename} after {max_retries} retries. Will not delete remote file.")

    # --- 5. Sleep before next cycle ---
    print(f"[{datetime.now()}] Sleeping for {interval/60} minutes before next check...\n")
    time.sleep(interval)
