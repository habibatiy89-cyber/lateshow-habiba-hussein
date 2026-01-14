Late Show API

A Flask REST API for managing Late Night Show episodes, guests, and appearances, built as part of the Phase 4 Code Challenge at Moringa School.

This API models the relationship between episodes and guests through appearances and exposes endpoints to retrieve and create data following a provided Postman collection.

Project Overview

The Late Show API allows you to:

View all episodes

View a single episode with its guest appearances

View all guests

Create new appearances linking guests to episodes with ratings

The application uses:

Flask

SQLAlchemy

Flask-Migrate

SQLite database

Data Models & Relationships
Models

Episode

Guest

Appearance

Relationships

An Episode has many Guests through Appearances

A Guest has many Episodes through Appearances

An Appearance belongs to one Episode and one Guest

Cascading deletes are enabled so that deleting an episode or guest removes related appearances.

Validations

The following validation is implemented:

Appearance.rating must be between 1 and 5 (inclusive)

Invalid data is rejected with appropriate error messages and HTTP status codes.

API Endpoints
GET /episodes

Returns a list of all episodes.

Response Example

[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]

GET /episodes/:id

Returns a single episode and its appearances.

Success Response

{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      }
    }
  ]
}


Error Response

{
  "error": "Episode not found"
}

GET /guests

Returns a list of all guests.

Response Example

[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
]

POST /appearances

Creates a new appearance linking an existing guest and episode.

Request Body

{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}


Success Response

{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}


Error Response

{
  "errors": ["validation errors"]
}

🗂️ Project Structure
lateshow-firstname-lastname/
├── server/
│   ├── models.py
│   ├── routes.py
│   ├── seed.py
│   ├── app.py
│   └── config.py
├── migrations/
├── instance/
│   └── app.db
├── challenge-4-lateshow.postman_collection.json
└── README.md

 Setup Instructions
 Clone the repository
git clone <your-repo-url>
cd lateshow-firstname-lastname

Install dependencies
pipenv install
pipenv shell

Run migrations
flask db init
flask db migrate
flask db upgrade

Seed the database
python server/seed.py

 Start the server
python server/app.py


The API will run at:

http://localhost:5555
