# Week 7: Socket Programming + Traffic Controller
## [Slides](https://docs.google.com/presentation/d/1QpdJfYfviVSs6KX31N2YLZhtOGRxh8wgLtubWHxPKAw/edit?usp=sharing)

## Docker ([installation](https://docs.mitmproxy.org/stable/overview-installation/))
### Basics:
The `Dockerfile` specifies the structure of a Docker `image`. The constructed `image` can then be used to spawn Docker `containers` which are running instances of whatever blueprint was defined in the `Dockerfile`.

### Files & Folders
- `Dockerfile`: Docker configuration file that specifies image.
- `start-simulator.sh`: Script file to remove, build, and run a new simulator. See comments inside file.
- `docker-script.sh`: Script that runs inside the container. Configures `tc` and starts the receiver code.
- `receiver.py`: The receiver socket code.
- `sender.py`: The sender socket code.
- `hdd`: Folder that acts as a hard disk for the Docker container.

### Getting Started
1. Put your receiver code inside `receiver.py`.
2. Make sure the right ports are exposed inside `start-simulator.sh` or `start-simulator.bat`.
3. Start your receiver code using `./start-simulator.sh` (Mac, Linux) or `./start-simulator.bat` (Windows).
4. Start your sender code using normal Python `python sender.py`.