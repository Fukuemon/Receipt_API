from domain.errors.errors import InternalServerError, NotFoundError, ValidationError
from fastapi import APIRouter

router = APIRouter()


@router.get("/health_check")
async def handle_error_test(error_type: str) -> dict:
    """
    ヘルスチェック用のエンドポイント。
    クエリパラメータ 'error_type' によって異なるエラーを発生させる。
    条件に当てはまらない場合は正常終了を返す。

    Args:
        error_type (str): 発生させたいエラータイプ
        ("validation", "not_found", "internal")
    """
    if error_type == "validation":
        raise ValidationError(description="入力値が不正です。")
    if error_type == "not_found":
        raise NotFoundError(description="リソースが見つかりませんでした。")
    if error_type == "internal":
        raise InternalServerError(description="処理中にエラーが発生しました。")
    return {"status": "ok"}
