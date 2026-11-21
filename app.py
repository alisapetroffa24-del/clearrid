import streamlit as st
st.set_page_config(
    page_title="Clearid",
    page_icon="✨",
    layout="wide"
)
# Назва проєкту

st.sidebar.title("✨ Clearid")
st.sidebar.write("Твій помічник для роботи з текстами")

# Навігація між сторінками
page = st.sidebar.radio(
    "Меню",
    [
        "Головна",
        "Скоротити текст",
        "Пояснити простими словами",
        "Витягти важливе",
        "Про проєкт"
    ]
)

# Демонстраційні результати

def show_result(function_name, text):
    """Показує демонстраційний результат роботи функції."""

    st.info(
        f"🔧 Заглушка: тут буде працювати AI-функція "
        f"«{function_name}». Після підключення штучного інтелекту "
        f"програма автоматично оброблятиме введений текст."
    )

    st.subheader("Демонстраційний результат")

    if function_name == "Скоротити текст":
        st.success(
            "Короткий зміст:\n\n"
            "• Текст містить основну інформацію про тему.\n"
            "• Головна думка — пояснення ключової проблеми.\n"
            "• Другорядні деталі можна не враховувати."
        )

    elif function_name == "Пояснити простими словами":
        st.success(
            "Пояснення простими словами:\n\n"
            "Це означає, що складну інформацію можна "
            "переформулювати простіше, щоб її було легше зрозуміти."
        )

    elif function_name == "Витягти важливе":
        st.success(
            "Важлива інформація:\n\n"
            "📅 Дата: 15 грудня\n\n"
            "⏰ Термін: до кінця тижня\n\n"
            "📌 Вимога: заповнити необхідну форму\n\n"
            "⭐ Головне: не пропустити встановлений термін."
        )


# Головна сторінка

if page == "Головна":

    st.title("✨ Clearid")
    st.subheader("Зроби складні тексти зрозумілими!")

    st.write(
        "Clearid — це програма, яка допомагає швидше "
        "розбиратися з великими та складними текстами."
    )

    st.divider()

    st.subheader("Що вміє Clearid?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ✂️")
        st.write("**Скорочення тексту**")
        st.write("Залишає тільки найважливішу інформацію.")

    with col2:
        st.markdown("### 💡")
        st.write("**Просте пояснення**")
        st.write("Допомагає зрозуміти складні слова та речення.")

    with col3:
        st.markdown("### 📌")
        st.write("**Пошук важливого**")
        st.write("Знаходить дати, терміни та основні вимоги.")

    st.divider()

    st.info("Обери потрібну функцію в меню зліва, щоб почати роботу.")


# Сторінка скорочення тексту

elif page == "Скоротити текст":

    st.title("✂️ Скорочення тексту")

    st.write(
        "Встав великий текст або завантаж файл. "
        "Clearid допоможе залишити головне."
    )

    uploaded_file = st.file_uploader(
        "Завантаж текстовий файл",
        type=["txt"],
        key="short_file"
    )

    text = ""

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8", errors="replace")

    text = st.text_area(
        "Або введи текст тут:",
        value=text,
        height=200,
        key="short_text"
    )

    length = st.selectbox(
        "Обери довжину результату:",
        ["Коротко", "Стандартно", "Детально"]
    )

    if st.button("✨ Скоротити текст", use_container_width=True):

        if text.strip() == "":
            st.warning("Спочатку введи текст або завантаж файл.")

        else:
            show_result("Скоротити текст", text)
            st.caption(f"Обрана довжина: {length}")


# Сторінка пояснення тексту

elif page == "Пояснити простими словами":

    st.title("💡 Пояснення простими словами")

    st.write(
        "Встав складний текст, щоб отримати його простіше пояснення."
    )

    uploaded_file = st.file_uploader(
        "Завантаж текстовий файл",
        type=["txt"],
        key="explain_file"
    )

    text = ""

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8", errors="replace")

    text = st.text_area(
        "Введи текст для пояснення:",
        value=text,
        height=200,
        key="explain_text"
    )

    if st.button("💡 Пояснити", use_container_width=True):

        if text.strip() == "":
            st.warning("Спочатку введи текст або завантаж файл.")

        else:
            show_result("Пояснити простими словами", text)


# Сторінка пошуку важливої інформації

elif page == "Витягти важливе":

    st.title("📌 Пошук важливої інформації")

    st.write(
        "Знайди в тексті дати, терміни, вимоги та головні факти."
    )

    uploaded_file = st.file_uploader(
        "Завантаж текстовий файл",
        type=["txt"],
        key="extract_file"
    )

    text = ""

    if uploaded_file is not None:
        text = uploaded_file.getvalue().decode("utf-8", errors="replace")

    text = st.text_area(
        "Введи текст для аналізу:",
        value=text,
        height=200,
        key="extract_text"
    )

    if st.button("📌 Знайти важливе", use_container_width=True):

        if text.strip() == "":
            st.warning("Спочатку введи текст або завантаж файл.")

        else:
            show_result("Витягти важливе", text)



# Інформація про проєкт

elif page == "Про проєкт":

    st.title("ℹ️ Про Clearid")

    st.write(
        "Clearid — навчальний проєкт, створений для "
        "полегшення роботи з великими текстами."
    )

    st.subheader("Основні можливості")

    st.markdown("""
    1. ✂️ Скорочення тексту.
    2. 💡 Пояснення складної інформації простими словами.
    3. 📌 Пошук дат, термінів та важливих фактів.
    """)

    st.divider()

    st.subheader("Як це працює?")

    st.write("""
    1. Користувач обирає потрібну функцію.
    2. Вводить текст або завантажує TXT-файл.
    3. Натискає кнопку обробки.
    4. Отримує результат.
    """)

    st.info(
        "Зараз це інтерактивний прототип. "
        "Штучний інтелект ще не підключений."
    )

    st.caption("Clearid © 2026")