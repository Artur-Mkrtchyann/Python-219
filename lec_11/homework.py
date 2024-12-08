import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def api_request(method, endpoint, data=None):
    """
    Generalized API request handler.
    """
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, json=data)
        response.raise_for_status()
        return response.json() if response.text else None
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"API request error: {e}")


def get_filtered_posts():
    """
    Fetch posts and filter based on criteria:
    - Titles with 6 or fewer words.
    - Bodies with 3 or fewer lines.
    """
    posts = api_request("GET", "/posts")
    filtered_posts = [
        post for post in posts
        if len(post["title"].split()) <= 6 and len(post["body"].split('\n')) <= 3
    ]
    print("\nFiltered GET results:")
    for post in filtered_posts:
        print(f"ID: {post['id']}, Title: {post['title']}")
    return filtered_posts


def create_post(title, body, user_id):
    """
    Create a new post.
    """
    new_post = {"title": title, "body": body, "userId": user_id}
    created_post = api_request("POST", "/posts", data=new_post)
    print("\nCreated POST result:")
    print(created_post)
    return created_post


def update_post(post_id, title, body, user_id):
    """
    Update an existing post.
    """
    updated_data = {"title": title, "body": body, "userId": user_id}
    updated_post = api_request("PUT", f"/posts/{post_id}", data=updated_data)
    print("\nUpdated PUT result:")
    print(updated_post)
    return updated_post


def delete_post(post_id):
    """
    Delete a post by ID.
    """
    api_request("DELETE", f"/posts/{post_id}")
    print(f"\nPost with ID {post_id} deleted successfully.")


if __name__ == "__main__":
    print("Starting API interactions...\n")

    # GET call with filtering
    filtered_posts = get_filtered_posts()

    # POST call
    created_post = create_post(
        title="Optimized Post Title",
        body="This is the body of the optimized post.",
        user_id=1
    )

    # PUT call
    updated_post = update_post(
        post_id=created_post["id"],
        title="Updated Optimized Post Title",
        body="This is the updated body of the post.",
        user_id=1
    )

    # DELETE call
    delete_post(post_id=created_post["id"])

    print("\nAll operations completed successfully.")
