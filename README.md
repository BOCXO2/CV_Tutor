# CV_Tutor
<h1 align="center">CV_Tutor</h1>

<p align="center">
  <em>Примеры работы с библиотеками Python для обработки изображений и визуализации данных.</em>
</p>

## Установка

<ol>
  <li>Клонируйте репозиторий:
    <pre><code>git clone https://github.com/BOCXO2/CV_Tutor.git</code></pre>
  </li>
  <li>Перейдите в директорию проекта:
    <pre><code>cd CV_Tutor</code></pre>
  </li>
  <li>Создайте виртуальное окружение и активируйте его (опционально):
    <pre><code>python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate</code></pre>
  </li>
  <li>Установите зависимости из файла <code>requirements.txt</code>:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

## Содержимое репозитория

<ul>
  <li><strong>main.py</strong> - Главный файл для запуска программы. Демонстрирует базовую обработку изображений с помощью библиотеки <code>cv2</code>.</li>
  <li><strong>visualize.py</strong> - Файл для визуализации данных. Использует <code>matplotlib</code> для построения графиков.</li>
  <li><strong>image_processing.py</strong> - Модуль с функциями для обработки изображений. Примеры: изменение размера, поворот, применение фильтров.</li>
  <li><strong>sample_data/</strong> - Директория с примерами изображений и данных, используемых для демонстрации работы программы.</li>
</ul>

## Как использовать

<ol>
  <li>Запустите <code>main.py</code> для выполнения основных операций обработки изображений:
    <pre><code>python main.py</code></pre>
  </li>
  <li>Используйте <code>visualize.py</code> для создания графиков и визуализации данных:
    <pre><code>python visualize.py</code></pre>
  </li>
  <li>Попробуйте изменить содержимое <code>image_processing.py</code> для изучения различных методов обработки изображений.</li>
</ol>

## Результаты

<p>
  После запуска файлов вы увидите:
</p>

<ul>
  <li>Обработанные изображения в окне <code>cv2.imshow</code> и сохраненные результаты в папке <code>output/</code>.</li>
  <li>Графики и диаграммы в отдельном окне, если используется <code>visualize.py</code>.</li>
</ul>

<p>Этот проект поможет вам изучить основы работы с изображениями и визуализацией данных на Python.</p>

