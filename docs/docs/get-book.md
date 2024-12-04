---
id: get-book
title: GET /books/book_id
sidebar_label: Retrieve Book Details
---

# GET /books/book_id

## Overview
Retrieve details of a specific book using its unique `book_id`.

## Request

### Path Parameters
| Parameter  | Type    | Required | Description                                |
|------------|---------|----------|--------------------------------------------|
| `book_id`  | integer | Yes      | The unique identifier for the book. Must be a positive integer. |

---

## Response

### Success
| Status Code | Description               |
|-------------|---------------------------|
| `200 OK`    | The book details were successfully retrieved. |

#### Example Response
```json
{
    "book_id": 1,
    "title": "Harry Potter and the Sorcerer's Stone",
    "author_firstname": "J.K.",
    "author_lastname": "Rowling",
    "genre": "Fantasy",
    "summary": "Eleven-year-old Harry discovers he’s a wizard and begins his magical education at Hogwarts, where he encounters friends, foes, and a quest to protect the Sorcerer’s Stone from falling into the wrong hands. In the end, Harry confronts Voldemort, who’s trying to regain power, and stops him for the first time."
}
```