import psycopg2
from adapters import PsqlBareString

conn = psycopg2.connect(user='postgres',database='postgres')

create_super_sql = """
create user %s with 
    superuser
    login
    encrypted password %s;
"""

role_sql = """
select * from pg_roles
"""

def run(sql, params):
    c = conn.cursor()
    res = c.execute(sql, params)
    conn.commit()
    return res

def fetch(sql, params = []):
    c = conn.cursor()
    res = c.execute(sql, params)
    return c.fetchall()

# past commands run:
#    res = run(create_super_sql, [PsqlBareString('testuser'), 'froofroo'])
#

if __name__ == '__main__':
    res = fetch(role_sql)
