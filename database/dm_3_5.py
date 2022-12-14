import inspect
import uuid
import records
import structlog
import time


def retrier(attempts=10):
    def get_function(fn):
        def get_args(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                response = fn(*args, **kwargs)
                print(f'Попытка выполнить запрос {attempt}')
                time.sleep(2)
                if len(response) > 0:
                    return response
            raise AssertionError(f"Не удалось выполнить запрос, в течении {attempts} попыток")

        return get_args

    return get_function


class DmDataBase:
    def __init__(self, host, dbname, port, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = records.Database(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}")
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='db')

    def close(self):
        self.db.close()

    def _send_query(self, query):
        log = self.log.bind(request_id=str(uuid.uuid4()))
        log.msg(
            'request',
            caller=inspect.stack()[2][3],
        )
        print(query)
        result = self.db.query(query)
        print(result.dataset)
        return result

    def _send_bulk_query(self, query):
        log = self.log.bind(request_id=str(uuid.uuid4()))
        log.msg(
            'request',
            caller=inspect.stack()[2][3],
        )
        print(query)
        self.db.bulk_query(query)

    @retrier(10)
    def get_all_users(self):
        query = '''
        SELECT * 
        FROM "public"."Users"
        '''
        rows = self._send_query(query).as_dict()
        return rows

    def delete_user_by_login(self, login):
        query = f'''
        DELETE  
        FROM "public"."Users"
        WHERE "Login" = '{login}'
        '''
        self._send_bulk_query(query)

    @retrier(10)
    def get_user_by_login(self, login):
        query = f'''
        SELECT * 
        FROM "public"."Users"
        WHERE "Login" = '{login}'
        '''
        rows = self._send_query(query).as_dict()
        return rows