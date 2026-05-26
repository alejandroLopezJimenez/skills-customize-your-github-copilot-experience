# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using the FastAPI framework. Students will create endpoints, handle request data, return JSON responses, and use Pydantic models for validation.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Create a basic FastAPI application and configure it to run with Uvicorn.

#### Requirements
Completed program should:

- Create a `FastAPI()` app instance in `starter-code.py`
- Add a root endpoint at `/` that returns a welcome message
- Include instructions for running the server with `uvicorn`

### 🛠️ Create Item Endpoints with Path and Query Parameters

#### Description
Add endpoints that return item data and accept both path and query parameters.

#### Requirements
Completed program should:

- Add a `GET /items/{item_id}` endpoint
- Accept an optional query parameter called `q`
- Return a JSON response containing `item_id`, `q`, and a sample description

### 🛠️ Add a POST Endpoint with Data Validation

#### Description
Use Pydantic to define a request model and implement a POST endpoint that accepts JSON data.

#### Requirements
Completed program should:

- Define a Pydantic model called `Item` with fields: `name`, `description`, and `price`
- Add a `POST /items/` endpoint that accepts an `Item`
- Return the posted item data with a new `item_id` field in the response

### 🛠️ Implement a Simple In-Memory Data Store

#### Description
Create a small in-memory store for items and add endpoints to create and read items.

#### Requirements
Completed program should:

- Use a Python dictionary to store item data by `item_id`
- Allow `POST /items/` to add new items to the store
- Allow `GET /items/{item_id}` to retrieve stored items
- Return a `404` error if the requested item is not found
