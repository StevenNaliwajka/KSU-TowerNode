#!/bin/bash

bash Codebase/Setup/create_global_config.sh
bash Codebase/Setup/create_sdr_config.sh
bash Codebase/Setup/create_atmospheric_config.sh
bash Codebase/Setup/install_python.sh
bash Codebase/Setup/create_venv.sh
bash Codebase/Setup/create_outfile.sh