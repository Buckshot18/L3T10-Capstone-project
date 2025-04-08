# Band Site Django Project

## Setup with Virtual Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/Buckshot18/L3T10-Capstone-project
   cd band_site

2. Create and activate virtual environment:
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

3. Install requirements:
    pip install -r requirements.txt

4. Run migrations
    python manage.py migrate

5. Run development server:
    python manage.py runserver

## Setup with Docker

1. Build image
    docker build -t band_site .

2. Run the container
    docker run -p 8000:8000 band_site

3. Access the site at
    http://localhost:8000
