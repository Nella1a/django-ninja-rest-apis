from ninja import Router

router = Router()

@router.get("/person")
def person(request):
    return "hello"


