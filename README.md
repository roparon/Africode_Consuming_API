# Africode Consuming API

This is a Flask-based web application that consumes and displays data from an external API. The application is designed with a responsive user interface using Bootstrap and includes several pages for displaying different types of data.

## Project Structure

### Key Files

- **`app.py`**: The main application file that initializes the Flask app and defines routes.
- **`templates/`**: Contains HTML templates for rendering pages.
  - `base.html`: The base template with a common layout for all pages.
  - Other templates (`index.html`, `users.html`, etc.) extend `base.html` and display specific content.
- **`static/styles.css`**: Custom CSS for styling the application.

## Features

- **Dynamic Navigation**: Links to different pages like Users, Posts, Comments, Photos, and Todos.
- **Responsive Design**: Built with Bootstrap for mobile-friendly layouts.
- **Template Inheritance**: Uses Flask's Jinja2 templating engine for reusable components.
- **API Integration**: Fetches and displays data from an external API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Africode_Consuming_API.git
   cd Africode_Consuming_API
2. Set up the environment:
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
3. Install the dependencis:
   pip install -r requirements.txt
4. Run the application:
   python app.py
5. Open your browser and navigate to http://127.0.0.1:5000.

   USAGE:
   
The application provides the following pages:

Home Page: Displays an overview of the app.
Users Page: Lists users fetched from the API.
Posts Page: Displays posts from the API.
Comments Page: Shows comments related to posts.
Photos Page: Displays photo albums.
Todos Page: Lists tasks and their statuses.
Dependencies
Flask
Bootstrap
Jinja2
External libraries (e.g., blinker, charset_normalizer, certifi)
License
This project is licensed under the MIT License. See the LICENSE file for details.
Collecting workspace information```markdown
# Africode Consuming API

This is a Flask-based web application that consumes and displays data from an external API. The application is designed with a responsive user interface using Bootstrap and includes several pages for displaying different types of data.

## Project Structure

```
Africode_Consuming_API/
├── app.py
├── myenv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
├── templates/
│   ├── album.html
│   ├── base.html
│   ├── comments.html
│   ├── index.html
│   ├── photos.html
│   ├── posts.html
│   ├── todos.html
│   └── users.html
└── static/
    └── styles.css
```

### Key Files

- **`app.py`**: The main application file that initializes the Flask app and defines routes.
- **`templates/`**: Contains HTML templates for rendering pages.
  - `base.html`: The base template with a common layout for all pages.
  - Other templates (`index.html`, `users.html`, etc.) extend `base.html` and display specific content.
- **`static/styles.css`**: Custom CSS for styling the application.

## Features

- **Dynamic Navigation**: Links to different pages like Users, Posts, Comments, Photos, and Todos.
- **Responsive Design**: Built with Bootstrap for mobile-friendly layouts.
- **Template Inheritance**: Uses Flask's Jinja2 templating engine for reusable components.
- **API Integration**: Fetches and displays data from an external API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Africode_Consuming_API.git
   cd Africode_Consuming_API
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

The application provides the following pages:

- **Home Page**: Displays an overview of the app.
- **Users Page**: Lists users fetched from the API.
- **Posts Page**: Displays posts from the API.
- **Comments Page**: Shows comments related to posts.
- **Photos Page**: Displays photo albums.
- **Todos Page**: Lists tasks and their statuses.

## Dependencies

- Flask
- Bootstrap
- Jinja2
- External libraries (e.g., `blinker`, `charset_normalizer`, `certifi`)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- External API for providing data.
```
