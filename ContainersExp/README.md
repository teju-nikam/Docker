# Docker Experiments — Source Code
## D.K.T.E Society's Textile and Engineering Institute, Ichalkaranji

All 7 Docker experiments (Kubernetes experiments excluded).

| Experiment | Topic | Key Files |
|---|---|---|
| exp1 | Installing and Exploring Docker | `exp1_commands.sh` |
| exp2 | Creating and Managing Docker Images | `app.py`, `Dockerfile`, `exp2_commands.sh` |
| exp3 | Containerizing a Python AI Application | `ml_app.py`, `requirements.txt`, `Dockerfile`, `exp3_commands.sh` |
| exp4 | Docker Volumes and Persistent Storage | `data_writer.py`, `data_reader.py`, `Dockerfile.writer`, `Dockerfile.reader`, `exp4_commands.sh` |
| exp5 | Docker Networking | `server.py`, `client.py`, `Dockerfile.server`, `Dockerfile.client`, `exp5_commands.sh` |
| exp6 | Multi-Container Apps (Docker Compose) | `app.py`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`, `exp6_commands.sh` |
| exp7 | Containerizing an ML Model | `train_model.py`, `predict_api.py`, `requirements.txt`, `Dockerfile`, `exp7_commands.sh` |

## Quick Start
Each experiment folder is self-contained. Navigate into the folder and run the shell script:
```bash
cd exp1 && bash exp1_commands.sh
```
