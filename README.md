# GitHub Dashboard



## Overview

The **GitHub Dashboard** is an interactive web application built with Python and Streamlit that visualizes and analyzes data from GitHub repositories. This dashboard provides insights into repository statistics such as issues count, stars count, and pull requests, making it easier for users to understand their GitHub activity.

## Features

- View repository statistics including issues count, stars count, and pull requests.
- Interactive visualizations for better understanding of the data.
- Easy navigation and user-friendly interface.
- Caching for improved performance and faster loading times.

## Installation

### Prerequisites

- Python 3.7 or later
- Git

### Clone the repository

```bash
git clone https://github.com/yourusername/github_dashboard.git
cd github_dashboard
Set up a virtual environment
bash
Copy code
python -m venv venv
Activate the virtual environment
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages
bash
Copy code
pip install -r requirements.txt
Usage
Running the app
To start the Streamlit app, run the following command:

bash
Copy code
streamlit run app.py
Accessing the dashboard
Open your web browser and navigate to http://localhost:8501 to view the dashboard.

Data
The dashboard uses a dataset (github_dataset.csv) that contains information about GitHub repositories. Make sure this file is present in the project directory. You can create your own dataset or modify the existing one as needed.
