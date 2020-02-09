import sqlalchemy as sa

b_id = {
  "name": "b_id",
  "type_": sa.BigInteger,
  "primary_key": True,
  "auto_increment": True,
}

b_key = {
  "name": "b_key",
  "type_": sa.Text,
}

b_hash = {
  "name": "b_hash",
  "type_": sa.Text,
  "index": True,
}

b_source_key = {
  "name": "b_source_key",
  "type_": sa.Text,
  "index": True,
}

b_source_value = {
  "name": "b_source_key",
  "type_": sa.Text,
  "index": True,
}

b_is_valid = {
  "name": "b_is_valid",
  "type_": sa.Boolean,
  "index": True,
}

b_created_by = {
  "name": "b_created_by",
  "type_": sa.Text,
}

b_created_ts = {
  "name": "b_created_ts",
  "type_": sa.DateTime,
}

b_touched_by = {
  "name": "b_touched_by",
  "type_": sa.Text,
}

b_touched_ts = {
  "name": "b_touched_ts",
  "type_": sa.DateTime,
}
