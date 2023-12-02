# Umbrella Platform

African households are disproportionately burdened by the perils of financial dependence, with a staggering majority relying solely on a single source of income, primarily salaried employment (World Bank, 2020). This reliance creates a precarious financial balance that leaves families highly vulnerable to unexpected expenses, economic fluctuations, and limited opportunities for wealth creation (AfDB, 2019).

Umbrella is a platform designed to diversify the incomes of African households by focusing on fractional ownership in real estate properties. 

## Tech Stack

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Backend:**
  - Python
  - Flask

- **Database:**
  - MySQL

## Project Structure

- **app.py:** The main application file.
  
- **connect.py:** Establishes a connection with the MySQL database.

- **basemodel.py:** Defines the base model, and other classes inherit from the base.

- /templates:** Contains all html files and templates.

- /static:** Contains all css and js codes, and a file storage directory for handling media files.


- **Other Files:**
  - *persisting.py:* creates a database session.
  - *portfolio.js:* Handles portfolio-related functionalities.
  - *user.js:* Manages user-related functionalities.

## Running the Application

To run the application, follow these steps: 

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Navigate to the project directory and run:
   You may need to set up a personal database on your local machine.
    ```bash
    cd umbrella-app
    python3 create_tables.py
    python3 superadmin.py
    ```

4. Run the application:
    ```bash
    python3 app.py
    ```

## Contributors

- Kingsley Budu Boafo

