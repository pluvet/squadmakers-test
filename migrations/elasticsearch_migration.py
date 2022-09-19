from source.infraestructure.elasticsearch import es

async def upgrade():
    await es.indices.create(index='joke')

async def downgrade():
    await es.options(ignore_status=[400,404]).indices.delete(index='test-index')