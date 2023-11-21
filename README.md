# Network Cell Modelling
## Getting Started
### Prerequisites
Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python 3.x installed on your system.

- **Docker**: Make sure you have Docker installed and run on your system.


### Installation
Clone the repository:

```shell
git clone https://github.com/Sashkow/nk-network-cell-modelling.git
cd nk-network-cell-modelling
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
docker-compose build
docker-compose up
```
The application should now be accessible at http://localhost:8000/.