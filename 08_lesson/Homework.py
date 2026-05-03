import pytest
import requests


class TestAPI:
    auth_token = (
        ""
    )  # вставить свой токен

    id_project = None

    base_url = "https://ru.yougile.com"
    project_name = "AutoGenProject"

    def _check_status_code(self, response, expected_codes):
        assert response.status_code in expected_codes

    @pytest.mark.order(1)
    def test_post(self):
        data = {"title": str(self.project_name), "users": {}}

        r = requests.post(
            self.base_url + "/api-v2/projects",
            headers={"Authorization": self.auth_token},
            data=data,
        )

        self._check_status_code(r, [200, 201])

        self.__class__.id_project = r.json()["id"]

    @pytest.mark.order(2)
    def test_post_negative(self):
        r = requests.post(
            self.base_url + "/api-v2/projects",
            headers={"Authorization": ""},
            data={"title": "InvalidProject"},
        )
        self._check_status_code(r, [401])

    @pytest.mark.order(3)
    def test_put(self):
        assert self.__class__.id_project is not None, "ID проекта не получен!"

        data = {"title": self.project_name + "_edited"}

        r = requests.put(
            self.base_url + "/api-v2/projects/" + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
            data=data,
        )

        self._check_status_code(r, [200])

    @pytest.mark.order(4)
    def test_put_negative(self):
        r = requests.put(
            self.base_url + "/api-v2/projects/invalid_project_id",
            headers={"Authorization": self.auth_token},
            data={"title": "InvalidProject"},
        )
        self._check_status_code(r, [404])

    @pytest.mark.order(5)
    def test_get(self):
        assert self.__class__.id_project is not None

        r = requests.get(
            self.base_url + "/api-v2/projects/" + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
        )

        self._check_status_code(r, [200])

    @pytest.mark.order(6)
    def test_get_negative(self):
        r = requests.get(
            self.base_url + "/api-v2/projects/123-invalid-id-456",
            headers={"Authorization": self.auth_token},
        )
        self._check_status_code(r, [404])


if __name__ == "__main__":
    pytest.main()
