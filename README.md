# 跑步單字練習 (Running Vocabulary Practice)

An interactive web application for practicing English vocabulary from Taiwan's university entrance exams (大學學測).

## Features

### 📚 Comprehensive Vocabulary Database
- **3000+ vocabulary words** from exam years 98-115
- Sourced from actual examination questions across multiple years
- Each entry includes English word and Chinese meaning

### 🎙️ Audio Support
- **Full pronunciation** for all vocabulary entries
- Bilingual audio: English (US accent) and Traditional Chinese (Taiwan accent)
- Adjustable playback speed (0.5x - 1.5x)
- Configurable pause interval between words (0.5s - 5s)

### 📊 Learning Tools
- **Year-based filtering**: Study specific exam years or all years
- **Shuffle mode**: Randomize question order for better retention
- **Progress tracking**: Visual progress bar and word counter
- **Question context**: View all options for each exam question
- **Navigation controls**: Move between words easily

### 🎯 Exam-Focused
- All vocabulary organized by exam question
- Option cards show context of multiple-choice answers
- Question numbering matches actual exam format

## Usage

### Basic Controls
- **Previous/Next**: Navigate between vocabulary words
- **Play**: Start automatic playback with audio pronunciation
- **Settings Panel**: Adjust year filter, speed, pause time, and shuffle mode

### Settings
| Setting | Range | Default |
|---------|-------|---------|
| Year Filter | All or specific years | All |
| Speech Rate | 0.5x - 1.5x | 0.85x |
| Pause Interval | 0.5s - 5s | 1.5s |
| Shuffle | On/Off | Off |

## Data Structure

Each vocabulary entry contains:
- **Year**: Exam year (e.g., 115)
- **Question Number**: Question ID (1-20)
- **English Word**: The vocabulary term
- **Chinese Translation**: Traditional Chinese meaning
- **Options**: Related words/synonyms from the exam question

Example:
```
[115, 1, "quashed", "推翻/撤銷", ["cosseted", "寵愛"], ["negotiated", "談判"], ...]
```

## Technical Details

### Technologies
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with glassmorphism design
- **Vanilla JavaScript**: No external dependencies
- **Web Speech API**: Native browser text-to-speech

### Browser Compatibility
- Requires modern browser with Web Speech API support
- Tested on Chrome, Safari, Edge

### File Size
- Single HTML file (self-contained)
- ~564 lines including 3000+ vocabulary entries

## Design Highlights

- **Glassmorphism UI**: Modern frosted glass effect with animated background orbs
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Easy on the eyes with gradient backgrounds
- **Smooth Animations**: Floating background elements and transitions

## Installation

No installation required! Simply:
1. Save `vocabulary_runner_full.html` locally
2. Open in any modern web browser
3. Start practicing!

## Tips for Effective Learning

1. **Consistent Practice**: Study 20-30 words per session
2. **Audio Learning**: Use audio playback to improve pronunciation
3. **Shuffle Mode**: Enable shuffle after learning to test retention
4. **Year-by-Year**: Start with recent years, then progress backward
5. **Multiple Runs**: Review difficult words repeatedly

## Future Enhancements

- [ ] Offline support with Service Worker
- [ ] User progress tracking and statistics
- [ ] Custom vocabulary lists
- [ ] Flashcard mode
- [ ] Quiz functionality with scoring
- [ ] Save/bookmark favorite words
- [ ] Mobile app version

## License

This project is provided as-is for educational purposes.

## Author

Created for Taiwan university entrance exam preparation.
