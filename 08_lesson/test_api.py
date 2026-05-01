import pytest
import requests


class TestAPI:
    auth_token = (
        "Bearer FsUSOrUEjC0p8vaY66q85KtfKW6-" "X0OrgoUhjWJ1jN5KjFScsjY1YiiDnT-L0TeB"
    )

    id_project = None

    base_url = "https://ru.yougile.com"
    project_name = "AutoGenProject"

    @pytest.mark.order(1)
    def test_post(self):
        data = {"title": str(self.project_name), "users": {}}

        r = requests.post(
            self.base_url + "/api-v2/projects",
            headers={"Authorization": self.auth_token},
            data=data,
        )

        assert r.status_code in [200, 201]
        self.__class__.id_project = r.json()["id"]

    @pytest.mark.order(2)
    def test_put(self):
        assert self.__class__.id_project is not None

        data = {
            "title": self.project_name + "_edited",
        }

        r = requests.put(
            self.base_url + "/api-v2/projects/" + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
            data=data,
        )

        assert r.status_code in [200]

    @pytest.mark.order(3)
    def test_get(self):
        assert self.__class__.id_project is not None

        r = requests.get(
            self.base_url + "/api-v2/projects/" + self.__class__.id_project,
            headers={"Authorization": self.auth_token},
        )

        assert r.status_code in [200]


if __name__ == "__main__":
    pytest.main()
