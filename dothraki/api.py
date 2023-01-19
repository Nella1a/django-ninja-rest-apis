from ninja import Router

router = Router()

@router.get("/ruler")
def ruler(request, gender):
    if gender == "m":
        return "Hello Khal"

    return "Hello Khaleesi"

@router.get("/horses")
def horses(request, num: int):
    horses = ["horse" for _ in range(num)]

    return "\n".join(horses)

