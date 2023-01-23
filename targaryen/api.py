from ninja import Router
from targaryen.schemas import DragonOut
router = Router()

@router.get("/dragons", response=list[DragonOut])
def dragon(request):
    data = [
        DragonOut(name="Dragon", birth_year=298),
        DragonOut(name="Rhaegal", birth_year=298),
        DragonOut(name="Viserion", birth_year=298),
    ]

    return data

