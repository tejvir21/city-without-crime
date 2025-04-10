# City Without Crime (CWC)

City Without Crime (CWC) is a Django-based web application designed to promote safety and transparency in urban areas. It empowers citizens to report crimes, track complaints, and collaborate with local authorities to build safer neighborhoods.

## Features

- **User Module**:
  - User registration and login.
  - Lodge complaints and track their status.

- **Police Station Module**:
  - Manage complaints assigned to the station.
  - Maintain criminal records.
  - Publish emergency news.

- **Admin Module**:
  - Manage police stations.
  - Oversee complaints and activities.

- **Emergency News**:
  - Publish and view emergency updates.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tejvir21/city-without-crime.git
   cd cwc
   ```
2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```
    python manage.py migrate
    ```
5. Run the development server:
    ```
    python manage.py runserver
    ```
6. Access the application at http://127.0.0.1:8000.

## Requirements

  - Python 3.8+
  - Django 5.1.5
  - SQLite (default database)

## Usage

  - **Admin**: Access the admin dashboard at ```/admin/```.
  - **Users**: Register, log in, and lodge complaints.
  - **Police Stations**: Log in to manage complaints and criminal records.

## Media and Static Files

  - Access the admin dashboard at ```media/```.
  - Static files are located in ```main/static/```.

## License

This project is licensed under the MIT License. See the ```LICENSE``` file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any inquiries, please contact [PORTFOLIO](https://tejvir.netlify.app/).
