from datetime import datetime, timezone
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Imagem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    status: str = "pendente"
    criada_em: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

engine = create_engine("postgresql+psycopg://tot:tot@localhost:5432/vddb")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(Imagem(nome="nota-fiscal.png"))
    session.commit()

    pendentes = session.exec(select(Imagem).where(Imagem.status == "pendente")).all()
    print(pendentes)
