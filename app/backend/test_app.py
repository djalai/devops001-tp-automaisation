import os
import tempfile
import pytest
from app import app, User

@pytest.fixture
def db():
   engine = create_engine(
       "sqlite:///:memory:", connect_args={"check_same_thread": False}
   )
   TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base.metadata.create_all(bind=engine)
   return TestSession()

@pytest.mark.parametrize(
   "id, name, email",
   [
       (1, "test", "test@example.com"),
       (2, "another", "another@example.com"),
   ],
)
def test_create_user(db, id, name, email, password):
   user_create = UserCreate(id=id, name=name, email=email)
   user = create_user(db, user_create)
   assert user.id == id
   assert user.name == name
   assert user.email == email

def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.test_create_user()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_get_users_empty(client):
    """ Test /users endpoint with empty database """
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == []

def test_get_users_with_data(client):
    """ Test /users endpoint with some data in the database """
    user = User(name='Test User', email='test@example.com')
    db.session.add(user)
    db.session.commit()

    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Test User'
    assert response.json[0]['email'] == 'test@example.com'

