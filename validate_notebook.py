"""Выполняет ноутбук целиком и проверяет сообщения встроенных тестов."""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import nbformat
from nbclient import NotebookClient

DEFAULT_NOTEBOOK = "MEPHI_RL26_hw1_VI_PI_Bujor_Alexandra.ipynb"
SUCCESS_MESSAGES = (
    "Поздравляем! Задание 1 выполнено корректно.",
    "Функция compute_value_function прошла тест.",
    "Функция extract_policy_from_v прошла тест.",
    "Поздравляем! Задание 2 выполнено корректно.",
    "Поздравляем! Задание 3 выполнено корректно.",
)


def validate(notebook_path: Path) -> None:
    notebook_path = notebook_path.resolve()
    if not notebook_path.is_file():
        raise FileNotFoundError(f"Ноутбук не найден: {notebook_path}")

    # Сохраняем графики непосредственно в выполненном ноутбуке.
    os.environ["MPLBACKEND"] = "module://matplotlib_inline.backend_inline"
    notebook = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        allow_errors=False,
        resources={"metadata": {"path": str(notebook_path.parent)}},
    )
    client.execute()

    output_text = "\n".join(
        output.get("text", "")
        for cell in notebook.cells
        if cell.cell_type == "code"
        for output in cell.get("outputs", [])
    )
    missing = [message for message in SUCCESS_MESSAGES if message not in output_text]
    if missing:
        raise AssertionError("Не найдены сообщения проверок: " + "; ".join(missing))

    nbformat.write(notebook, notebook_path)
    executed_cells = sum(
        cell.cell_type == "code" and cell.get("execution_count") is not None
        for cell in notebook.cells
    )
    figures = sum(
        output.get("output_type") == "display_data"
        and "image/png" in output.get("data", {})
        for cell in notebook.cells
        if cell.cell_type == "code"
        for output in cell.get("outputs", [])
    )
    print(f"OK: {notebook_path.name}")
    print(f"Выполнено кодовых ячеек: {executed_cells}; графиков сохранено: {figures}.")
    print("Все встроенные assert-проверки заданий 1–3 пройдены.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", nargs="?", default=DEFAULT_NOTEBOOK, type=Path)
    args = parser.parse_args()
    validate(args.notebook)
