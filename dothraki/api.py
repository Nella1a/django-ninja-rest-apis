from ninja import Router

router = Router()

@router.get("/ruler")
def ruler(request, gender):
    if gender == "m":
        return "Hello Khal"

    return "Hello Khaleesi"