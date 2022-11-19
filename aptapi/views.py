import fastapi
from starlette.responses import Response
from fastapi import Request
from .queries import *


router = fastapi.APIRouter()


@router.get('/api/apartments/')
async def apartments(id: int=None):
    if id:
        apt = await get_apt_by_id(await get_session(), id)
        resp = await process_objects(apt)
        return Response(resp)
    else:
        apts = await get_all_apts(await get_session())
        resp = await process_objects(apts)
        return Response(resp)


@router.get('/api/apartments/filter/')
async def apartments(request: Request):
    kwargs = request.query_params
    apts = await get_apt_filters(await get_session(), **kwargs)
    if apts == 'Wrong data input':
        return apts
    resp = await process_objects(apts)
    return Response(resp)

