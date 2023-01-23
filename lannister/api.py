from ninja import Router


router = Router()

# define an api-path-endpoint
@router.get("/home")
def home(request):
    return "A Lannster always pays their debts"