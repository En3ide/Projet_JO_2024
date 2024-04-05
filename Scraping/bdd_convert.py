def convert_maria_to_postgresql(sql):
    sql = sql.replace("IGNORE", "")
    sql = sql.replace(");", ") ON CONFLICT DO NOTHING;")
    return sql