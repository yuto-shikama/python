import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import APIRouter
import awsCliUtil


router = APIRouter()

@router.get("/awsCli/getS3", tags=["AWS"])
async def read_user_me():
    return awsCliUtil.aws_ls("")