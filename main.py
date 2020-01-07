"""Application entry point."""
from ghost_sql_sanitation import main
from flask import request

if __name__ == '__main__':
    main(request)
