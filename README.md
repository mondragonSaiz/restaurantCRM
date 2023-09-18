# Restaurant Listing CRM Project

This is a Django-based project that allows users to view a list of restaurants, log in, add new restaurants, and perform CRUD (Create, Read, Update, Delete) operations on restaurant entries.

## Installation

Follow these steps to set up and run the project on your local machine:

### Prerequisites

- Python 3.x installed (you can download it from [Python's official website](https://www.python.org/downloads/))
- pip package manager installed (usually comes with Python)
- MySQL installed and configured

### Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-listing-crm.git
cd restaurant-listing-crm
```


### Virtual Environment (Optional but Recommended)
It's a good practice to create a virtual environment to isolate project dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### Install Dependencies
- Create a MySQL database for your project.
- Update the database settings in settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Or your database host
        'PORT': '',           # 3306 for default MySQL port
    }
}
```
 - Apply migrations to create the database tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Create a Superuser (Admin)

You can create an admin user who can add, update, and delete restaurants through the Django admin interface.
 ```bash
python manage.py createsuperuser
```

### Running the Development Server

```bash
python manage.py runserver
```

The development server will start, and you can access the project in your web browser at http://127.0.0.1:8000/.

## Usage
- Access the restaurant listing at http://127.0.0.1:8000/.
- Log in with your superuser credentials at http://127.0.0.1:8000/admin/ to access the admin panel for CRUD operations on restaurants.
- Creating an account is required to make changes (CRUD) in restaurant list.

##  Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository
- Create your branch: git checkout -b feature/your-feature
- Make your changes and commit them: git commit -m 'Add some feature'
- Push to the branch: git push origin feature/your-feature
- Create a pull request

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
* Django -  web framework used
* MySQL -  database used
  
Feel free to customize this README file according to your project's specific details and requirements. It's important to provide clear and concise instructions so that others can easily set up and use your project.



<img width="1408" alt="Screen Shot 2023-09-17 at 23 38 33" src="https://github.com/mondragonSaiz/restaurantCRM/assets/71055501/fc3fed87-69d4-44e6-9982-ee6782c20481">




<img width="1418" alt="Screen Shot 2023-09-17 at 23 39 50" src="https://github.com/mondragonSaiz/restaurantCRM/assets/71055501/1cbed67d-6739-4a9f-9ed8-e37a69343aa0">



   
  
