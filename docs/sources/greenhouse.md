# Greenhouse

[Job Board API documentation](https://docs.greenhouse.io/job-board.html#introduction)

## Base URL and authentication

`https://boards-api.greenhouse.io/v1/boards/{board_token}`

Public GET endpoints do not require authentication. `board_token` identifies a Greenhouse job board.

## Endpoints

### List jobs

`GET /v1/boards/{board_token}/jobs`

| Parameter | Location | Description |
| --- | --- | --- |
| `board_token` | Path | Board identifier. |
| `content=true` | Query | Includes posting descriptions, departments, and offices. |

The response contains job postings with fields such as `id`, `title`, `location.name`, `absolute_url`, `updated_at`, and `metadata`. With `content=true`, postings also include `content`, `departments`, and `offices`. The documented example includes `meta.total`.

### Retrieve a job

`GET /v1/boards/{board_token}/jobs/{job_id}`

| Parameter | Location | Description |
| --- | --- | --- |
| `board_token` | Path | Board identifier. |
| `job_id` | Path | Job post ID, as returned by the list endpoint. |
| `questions=true` | Query | Adds application-form fields to the response. |

The default response includes fields such as `id`, `title`, `location.name`, `absolute_url`, `updated_at`, `content`, and `metadata`. The documentation does not establish whether `departments` or `offices` are present in this response.

## API behavior

The linked documentation does not specify pagination or a rate-limit policy for these job-reading endpoints.
