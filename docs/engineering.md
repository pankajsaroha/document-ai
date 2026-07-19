# Engineering rules

1. Only the ApplicationContainer creates shared dependencies.

2. No os.getenv() outside settings.py

3. Business logic must not depend on FastAPI

4. Constructor dependency injection only

5. Every class has a single responsibility.