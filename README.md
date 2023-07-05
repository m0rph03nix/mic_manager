# mic_manager

## Lancement


- **Mic service** 
```bash
rosrun mic_manager capture.py
```

- **Call the service** 
```bash
rosservice call mic_capture "data: true" # Authorise la capture de son
rosservice call mic_capture "data: false" # Coupe la capture de son

```

- **Pour se lancer depuis un code python, importez ce srv standard**
```python
from std_srvs.srv import SetBool, from std_srvs.srv import SetBool, SetBoolAnswer
```