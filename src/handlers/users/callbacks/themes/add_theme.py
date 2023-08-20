from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from src.bot.fsm.add_theme_fsm import AddTheme
from src.data import callback_answers
from src.keyboards.common_keyboards import create_finish_inline_keyboard
from src.models.ThemeModel import ThemeModelToWrite, ThemesLinksModel
from src.requests.themes import add_new_theme
from src.utils.exception import RequestException

router = Router(name="router_add_theme")


@router.callback_query(lambda x: x.data == callback_answers.ADD_THEME)
async def add_theme_start(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    """"""
    finish_keyboard = create_finish_inline_keyboard(name="создание новой темы")

    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        text="Введите название темы",
        reply_markup=finish_keyboard.as_markup()
    )
    await callback_query.message.delete()
    await state.set_state(AddTheme.write_theme_name)
    return


@router.message(AddTheme.write_theme_name)
async def add_theme_get_theme_name(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(theme_name=msg.text)
    await msg.answer("Введите описание темы")
    await state.set_state(AddTheme.write_theme_description)


@router.message(AddTheme.write_theme_description)
async def add_theme_get_theme_description(msg: types.Message, state: FSMContext) -> None:
    theme_description = msg.text
    user_data = await state.get_data()
    try:
        theme = ThemeModelToWrite(
            name=user_data["theme_name"],
            description=theme_description,
            links=ThemesLinksModel(
                user_id=str(msg.from_user.id)
            )
        )
        await add_new_theme(theme)
        await msg.answer(f'Тема "{user_data["theme_name"]}" успешно сохранена')

    except RequestException as err:
        await msg.answer("Что-то пошло не так, попробуйте позже =(")

    await state.clear()
    return None
