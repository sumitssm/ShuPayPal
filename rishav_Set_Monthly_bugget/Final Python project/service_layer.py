from setBalance import give_value
from balance_repository import balanceRepository

bal=setbalance()
repo=balanceRepository(bal)
console = Console(repo)
console.render()
