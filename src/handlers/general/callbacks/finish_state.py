from aiogram import types
from aiogram.fsm.context import FSMContext


async def finish_state(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """Finish all active fsm state"""
    await callback_query.message.delete()
    await state.clear()
