import requests

res = requests.get("https://jsonplaceholder.typicode.com/users")
print(res.status_code)

dv = res.json()
print(dv)




'''

| Status Code                    | Meaning                      | When it's used                                           |
| ------------------------------ | ---------------------------- | -------------------------------------------------------- |
| **200 OK**                     | Success                      | Request completed successfully                           |
| **201 Created**                | Resource created             | POST request created a new resource                      |
| **202 Accepted**               | Accepted                     | Request accepted for processing but not completed yet    |
| **204 No Content**             | Success, no response body    | DELETE or successful update with no content returned     |
| **301 Moved Permanently**      | Redirect                     | Resource has a new permanent URL                         |
| **302 Found**                  | Temporary redirect           | Resource temporarily available elsewhere                 |
| **304 Not Modified**           | Cached version valid         | Client can use cached resource                           |
| **400 Bad Request**            | Invalid request              | Missing or invalid parameters, malformed JSON            |
| **401 Unauthorized**           | Authentication required      | Missing or invalid authentication token                  |
| **403 Forbidden**              | Access denied                | User is authenticated but lacks permission               |
| **404 Not Found**              | Resource not found           | Requested endpoint or resource doesn't exist             |
| **405 Method Not Allowed**     | HTTP method not supported    | For example, using POST on a GET-only endpoint           |
| **409 Conflict**               | Conflict                     | Duplicate resource or conflicting request                |
| **410 Gone**                   | Resource permanently removed | Resource no longer exists                                |
| **415 Unsupported Media Type** | Invalid content type         | For example, sending XML when JSON is expected           |
| **422 Unprocessable Entity**   | Validation failed            | Input is syntactically correct but contains invalid data |
| **429 Too Many Requests**      | Rate limit exceeded          | Client sent too many requests                            |
| **500 Internal Server Error**  | Server error                 | Unexpected server-side failure                           |
| **501 Not Implemented**        | Feature not supported        | Server doesn't support the requested functionality       |
| **502 Bad Gateway**            | Upstream server error        | Gateway received an invalid response                     |
| **503 Service Unavailable**    | Service unavailable          | Server is overloaded or under maintenance                |
| **504 Gateway Timeout**        | Upstream timeout             | Gateway didn't receive a timely response                 |

'''