from functools import wraps
from datetime import datetime

# Role -> allowed permissions
ROLES = {
    "data_engineer": {"extract", "transform"},
    "data_scientist": {"transform", "train", "evaluate"},
    "ml_engineer": {"train", "evaluate", "deploy"},
    "admin": {"extract", "transform", "train", "evaluate", "deploy"},
    "viewer": {"view"},
}

# Audit log
AUDIT_LOG = []


class AccessDenied(Exception):
    """Raised when a role is not authorized."""
    pass


def audit(role, permission, allowed):
    entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "role": role,
        "action": permission,
        "result": "ALLOW" if allowed else "DENY",
    }

    AUDIT_LOG.append(entry)


def require(permission):
    """Decorator that enforces RBAC."""

    def decorator(func):

        @wraps(func)
        def wrapper(user_role, *args, **kwargs):

            allowed = permission in ROLES.get(user_role, set())

            # Record every decision
            audit(user_role, permission, allowed)

            if not allowed:
                raise AccessDenied(
                    f"Role '{user_role}' is NOT authorized for '{permission}'"
                )

            print(f"[AUTH OK ] {user_role:15s} -> {permission}")

            return func(user_role, *args, **kwargs)

        return wrapper

    return decorator


@require("extract")
def extract(role):
    return "raw_data"


@require("train")
def train(role):
    return "trained_model"


@require("deploy")
def deploy(role):
    return "deployed"


def try_action(fn, role):
    try:
        fn(role)
    except AccessDenied as e:
        print(f"[DENIED ] {e}")


if __name__ == "__main__":

    print("=== ML Pipeline Access Control ===")

    # Admin is allowed
    extract("admin")
    train("admin")
    deploy("admin")

    # These should be denied
    try_action(deploy, "data_scientist")
    try_action(train, "viewer")
    try_action(extract, "ml_engineer")

    print("\n=== Audit Log ===")

    for e in AUDIT_LOG:
        print(
            f"{e['time']} "
            f"{e['role']:15s} "
            f"{e['action']:10s} "
            f"{e['result']}"
        )