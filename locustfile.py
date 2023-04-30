from locust import FastHttpUser, task



class MoviesUser(FastHttpUser):

    HEADERS = {
        'Authorization': 'Token  <Auth Token>'
    }

    @task
    def movie_search(self):
        self.client.get(
            "/api/movies/?genre=comedy",
            headers = self.HEADERS
        )


