import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Student, Course

@pytest.fixture
def client():
    return APIClient()
@pytest.fixture
def factory_student():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory
@pytest.fixture
def factory_courses():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_first_course(client, factory_courses):
    # Arrange
    courses = factory_courses(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/{courses[0].id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert type(data)==dict
    assert data['id'] == courses[0].id

@pytest.mark.django_db
def test_get_list_course(client, factory_courses):
    # Arrange
    courses = factory_courses(_quantity=10)

    # Act
    response = client.get(f'/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data)==len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name

@pytest.mark.django_db
def test_filter_id_course(client, factory_courses):
    # Arrange
    courses = factory_courses(_quantity=10)
    element = courses[5].id
    # Act
    response = client.get(f'/api/v1/courses/{element}/')
    response_filtred = client.get(f'/api/v1/courses/?id={element}')

    # Assert
    data_filtred = response_filtred.json()
    data = response.json()

    assert type(data)==dict
    assert data == data_filtred[0]
    assert (data_filtred[0]['id']) == element

@pytest.mark.django_db
def test_filter_name_course(client, factory_courses):
    # Arrange
    courses = factory_courses(_quantity=10)
    element = courses[5].name

    # Act
    response_filtred = client.get(f'/api/v1/courses/?name={element}')

    # Assert
    data_filtred = response_filtred.json()

    assert type(data_filtred)==list
    assert (data_filtred[0]['name']) == element

@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    count = Course.objects.count()
    data = {"name": "name_test"}

    # Act
    response = client.post('/api/v1/courses/', data=data)

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, factory_courses):
    # Arrange
    courses = factory_courses(_quantity=10)
    element = courses[5].id
    data = {"name": "test_name_course"}

    # Act
    response_update = client.patch(f'/api/v1/courses/{element}/', data=data)

    # Assert
    data_updated = response_update.json()

    assert response_update.status_code == 200
    assert data_updated['name'] == data['name']

#
@pytest.mark.django_db
def test_delete_course(client, factory_courses):
    # Arrange
    courses = factory_courses(_quantity=10)
    element = courses[5].id
    count = Course.objects.count()

    # Act
    response_delete = client.delete(f'/api/v1/courses/{element}/')

    # Assert
    assert response_delete.status_code == 204
    assert Course.objects.count() == count - 1