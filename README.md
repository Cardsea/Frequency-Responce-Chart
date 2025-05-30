# Frequency Response Chart Generator

This Python application generates a frequency response chart by playing and recording a frequency sweep (chirp) signal through your audio system. It's useful for testing audio equipment and room acoustics.

## Requirements

- Python 3 or higher
- A working audio input/output setup (microphone and speakers)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Cardsea/Frequency-Response-Chart.git
cd Frequency-Response-Chart
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your audio input (microphone) and output (speakers) are properly connected and selected in your system settings.

2. Run the program:
```bash
python main.py
```

3. The program will:
   - Generate a logarithmic frequency sweep from 20 Hz to 20 kHz
   - Play the sweep through your speakers
   - Record the response through your microphone
   - Generate a frequency response plot

## Configuration

You can modify the following parameters in `main.py`:
- `duration`: Length of the frequency sweep (default: 2 seconds)
- `fs`: Sample rate (default: 44100 Hz)
- `f_start`: Starting frequency (default: 20 Hz)
- `f_end`: Ending frequency (default: 20000 Hz)

## Output

The program will display a plot showing the frequency response of your system, with:
- X-axis: Frequency (Hz) in logarithmic scale
- Y-axis: Amplitude (RMS)

## Notes

- For best results, ensure a quiet environment during measurement
- Keep the microphone at a consistent distance from the speakers
- Avoid clipping (audio distortion) by adjusting your system's volume appropriately 