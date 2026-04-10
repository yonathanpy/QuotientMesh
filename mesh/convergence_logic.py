class ConvergenceLogic:
    def __init__(self):
        self._state_versions = {}

    def update(self, node: str, version: int):
        current = self._state_versions.get(node, 0)

        if version > current:
            self._state_versions[node] = version
            return True

        return False

    def snapshot(self):
        return dict(self._state_versions)
