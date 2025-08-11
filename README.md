# PyConc - Python Concurrency Examples

A comprehensive collection of Python concurrency examples demonstrating common problems, solutions, and advanced patterns using thread pools and polling strategies.

## 🎯 Purpose

This project serves as both a learning resource and a practical toolkit for understanding Python concurrency concepts. It demonstrates:

- **Common Concurrency Problems**: Deadlock, livelock, and starvation scenarios
- **Problem Solutions**: Multiple approaches to resolve each concurrency issue
- **Advanced Patterns**: Thread pool implementations with various polling strategies
- **Best Practices**: Proper thread management, error handling, and resource coordination

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ (uses `concurrent.futures.ThreadPoolExecutor`)
- No external dependencies required

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd pyconc

# Run examples directly
python3 pyconc.py -e deadlock
python3 pyconc.py -e threadpool-polling-adaptive
```

## 📚 Available Examples

### Deadlock Examples
| Example | Description | Command |
|---------|-------------|---------|
| **Problem** | Classic dining philosophers deadlock | `python3 pyconc.py -e deadlock` |
| **Resource Ordering Fix** | Prevent deadlock through consistent lock ordering | `python3 pyconc.py -e deadlock-fix-resource-ordering` |
| **Timeout Fix** | Break deadlock with timeout mechanisms | `python3 pyconc.py -e deadlock-fix-timeout` |
| **Asymmetric Behavior** | Different strategies for different philosophers | `python3 pyconc.py -e deadlock-fix-asymmetric-behavior` |
| **Waiter Solution** | Centralized resource management | `python3 pyconc.py -e deadlock-fix-waiter` |

### Livelock Examples
| Example | Description | Command |
|---------|-------------|---------|
| **Problem** | Polite threads stuck in endless loops | `python3 pyconc.py -e livelock` |
| **Random Backoff Fix** | Break livelock with randomized delays | `python3 pyconc.py -e livelock-fix-random-backoff` |
| **Priority Fix** | Assign priorities to break symmetry | `python3 pyconc.py -e livelock-fix-priority` |

### Starvation Examples
| Example | Description | Command |
|---------|-------------|---------|
| **Problem** | Some threads perpetually denied resources | `python3 pyconc.py -e starvation` |
| **Fair Scheduling Fix** | Ensure equal access to resources | `python3 pyconc.py -e starvation-fix-fair-scheduling` |
| **Aging Fix** | Increase priority of waiting threads | `python3 pyconc.py -e starvation-fix-aging` |

### ThreadPool Examples
| Example | Description | Command |
|---------|-------------|---------|
| **Basic** | Fundamental ThreadPoolExecutor usage | `python3 pyconc.py -e threadpool` |
| **Periodic Polling** | Fixed-interval task execution | `python3 pyconc.py -e threadpool-polling-periodic` |
| **Adaptive Polling** | Load-aware interval adjustment | `python3 pyconc.py -e threadpool-polling-adaptive` |
| **Event-Driven** | Priority-based event processing | `python3 pyconc.py -e threadpool-polling-event-driven` |
| **Batch Processing** | Grouped item processing | `python3 pyconc.py -e threadpool-polling-batch` |

## 🛠️ Usage

### Command Line Interface
```bash
# Basic usage
python3 pyconc.py -e <example-name>

# With custom duration (default: 5 seconds)
python3 pyconc.py -e deadlock -d 10

# Show help
python3 pyconc.py -h
```

### Running Individual Examples
Each example can be run independently:
```bash
# Run specific examples directly
python3 examples/deadlock/deadlock_problem.py
python3 examples/threadpool/threadpool_polling_periodic.py
```

### Customizing Examples
Most examples accept parameters for customization:
```python
# In your own code
from examples.deadlock import DeadlockExample

example = DeadlockExample(num_philosophers=10)
example.run(duration=15)
```

## 🏗️ Project Structure

```
pyconc/
├── pyconc.py                    # Main command-line interface
├── README.md                    # This file
├── requirements.txt             # Dependencies (none currently)
├── setup.py                     # Package installation
├── examples/                    # Examples package
│   ├── __init__.py             # Main examples package
│   ├── deadlock/               # Deadlock examples
│   │   ├── __init__.py
│   │   ├── deadlock_problem.py
│   │   └── deadlock_fix_*.py
│   ├── livelock/               # Livelock examples
│   │   ├── __init__.py
│   │   ├── livelock_problem.py
│   │   └── livelock_fix_*.py
│   ├── starvation/             # Starvation examples
│   │   ├── __init__.py
│   │   ├── starvation_problem.py
│   │   └── starvation_fix_*.py
│   └── threadpool/             # ThreadPool examples
│       ├── __init__.py
│       ├── threadpool_problem.py
│       └── threadpool_polling_*.py
└── tests/                       # Test suite
    ├── __init__.py
    ├── test_deadlock.py
    ├── test_livelock.py
    ├── test_starvation.py
    └── test_threadpool.py
```

## 🔍 Understanding the Examples

### Deadlock (Dining Philosophers)
- **Problem**: Five philosophers sit around a table with one fork between each pair
- **Deadlock**: Each philosopher picks up one fork and waits forever for the second
- **Solutions**: Resource ordering, timeouts, asymmetric behavior, centralized management

### Livelock (Polite Threads)
- **Problem**: Two threads trying to be polite, constantly yielding to each other
- **Livelock**: Endless loop of "after you" without progress
- **Solutions**: Random backoff, priority assignment

### Starvation (Resource Hogging)
- **Problem**: Some threads monopolize resources, others never get access
- **Starvation**: Perpetual denial of resource access
- **Solutions**: Fair scheduling, aging mechanisms

### ThreadPool Polling Strategies
- **Periodic**: Fixed intervals for monitoring and scheduled tasks
- **Adaptive**: Dynamic intervals based on system load
- **Event-Driven**: Priority-based processing of external events
- **Batch**: Efficient processing of grouped items

## 🧪 Testing

### Run All Tests
```bash
python3 -m pytest tests/
```

### Run Specific Test Categories
```bash
python3 -m pytest tests/test_deadlock.py
python3 -m pytest tests/test_threadpool.py
```

### Test with Coverage
```bash
python3 -m pytest --cov=examples tests/
```

## 📖 Learning Path

### Beginner
1. Start with basic examples: `deadlock`, `livelock`, `starvation`
2. Understand the problems and why they occur
3. Run examples with different durations to observe behavior

### Intermediate
1. Study the fix implementations
2. Modify parameters to see how solutions scale
3. Run multiple examples simultaneously to compare

### Advanced
1. Examine the code structure and design patterns
2. Create your own variations of the examples
3. Integrate patterns into your own projects

## 🤝 Contributing

### Adding New Examples
1. Create a new file in the appropriate `examples/` subdirectory
2. Follow the existing naming convention
3. Update the relevant `__init__.py` files
4. Add to `pyconc.py` command-line interface
5. Include tests in the `tests/` directory

### Code Style
- Follow PEP 8 guidelines
- Include comprehensive docstrings
- Add type hints where appropriate
- Ensure examples are self-contained and runnable

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by classic computer science problems
- Built with Python's standard library concurrency tools
- Designed for educational and practical use

## 🔗 Related Resources

- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [Concurrent Futures Documentation](https://docs.python.org/3/library/concurrent.futures.html)
- [Real Python Concurrency Tutorial](https://realpython.com/python-concurrency/)
- [Python Concurrency Patterns](https://python-patterns.guide/concurrency/)

---

**Happy Learning! 🐍✨** 