# PHD2 Badge Interaction Console Program

This is a console program designed to interact with the PHD2 badge. It is written in Python 3.12 and utilizes the `requests` and `numpy` libraries. The project is managed and installed using `poetry`.

## Requirements

- Python 3.12
- `poetry` for dependency management
- `requests` library
- `numpy` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/D0Nater/PHD2-Badge.git
   ```

2. **Install dependencies using `poetry`:**

   ```bash
   poetry install
   ```

3. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```

## Usage

To run the program, use the following commands:

```bash
phd run --help
```

### Text module

The `phd run text` command is part of the phd CLI tool, which allows you to run text animations with various options. Below is a detailed description of the command and its options.

Using the command:

```bash
phd run text --help
```

#### Options for text module

**`--text` / `-t`** : This option allows you to specify the text that will be animated. The default value is :zov:. You can use any string, but here are some examples: "i:heart:python", ":phd2:", ":zov:", ":svo:", ":mom:".

**`--mode` / `-m`**: This option sets the animation mode. Default mode — `sliderLeft`. Available modes: `switching` , `sliderUp` , `sliderLeft` .

**`--delay` / `-d`**: This option specifies the delay between animation frames in seconds. The default value — `0.15`.

**`--repeats` / `-r`**: This option sets the number of repetitions of the animation. The default value — `-1`, which means an endless repetition of the animation.

#### Example for text module

[Video 1](./media/text1.mp4)  [Video 2](./media/text2.mp4)

To start a text animation with custom options, you can use the following command:

```bash
phd run text --text ":mom:" --mode "sliderLeft" --delay 0.1 --repeats 10
```

### Snake module

The `phd run snake` command is part of the phd CLI tool, which allows you to run snake game with various options. Below is a detailed description of the command and its options.

Using the command:

```bash
phd run snake --help
```

#### Options for snake module

**`--delay` / `-d`**: This option specifies the delay between animation frames in seconds. The default value — `6`.

#### Example for snake module

[Video](./media/snake.mp4)

To start a snake game with custom options, you can use the following command:

```bash
phd run snake --delay 7
```

### Matrix module

The `phd run matrix` command is part of the phd CLI tool, which allows you to run matrix animation with various options. Below is a detailed description of the command and its options.

Using the command:

```bash
phd run matrix --help
```

#### Options for matrix module

**`--delay` / `-d`**: This option specifies the delay between animation frames in seconds. The default value — `0.1`.

**`--frequency` / `-f`**: This option specifies the frequency of drops (0 <= n <= 1). The default value — `0.2`.

#### Example for matrix module

[Video](./media/matrix.mp4)

To start a matrix animation with custom options, you can use the following command:

```bash
phd run matrix --delay 0.07 --frequency 0.1
```
