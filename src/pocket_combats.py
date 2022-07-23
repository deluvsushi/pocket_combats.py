import requests

class PocketCombats:
	def __init__(self):
		self.api = "https://game.pocketcombats.com"
		self.headers = {
			"user-agent": "okhttp/3.10.0",
			"content-type": "application/json"}
		self.auth_token = None

	def register(
			self, 
			google_id_token: str, 
			username: str, 
			gender: str = "MALE", 
			sdk_version: int = 238, 
			vendor: str = "samsung SM-N976N 7.1.2"):
		data = {
			"gender": gender,
			"id_token": google_id_token,
			"sdk_version": sdk_version,
			"username": username,
			"vendor": vendor
		}
		return requests.post(
			f"{self.api}/api/register", 
			data=data, 
			headers=self.headers).json()

	def register_new_character(
			self,
			google_id_token: str,
			username: str,
			gender: str = "MALE",
			sdk_version: int = 238,
			vendor: str = "samsung SM-G9880 7.1.2"):
		data = {
			"gender": gender,
			"id_token": google_id_token,
			"sdk_version": sdk_version,
			"username": username,
			"vendor": vendor
		}
		return requests.post(
			f"{self.api}/auth/register", 
			json=data, 
			headers=self.headers).json()

	def login_with_token(self, auth_token: str):
		self.auth_token = auth_token
		self.headers["authorization"] = f"Bearer {self.auth_token}"
		return self.auth_token

	def get_chat_history(self):
		return requests.post(
			f"{self.api}/api/chat/history",
			headers=self.headers).json()

	def get_chat_channels(self):
		return requests.get(
			f"{self.api}/api/chat/channels",
			headers=self.headers).json()

	def get_current_player(self):
		return requests.get(
			f"{self.api}/api/player/self",
			headers=self.headers).json()

	def get_location_info(self):
		return requests.get(
			f"{self.api}/api/location",
			headers=self.headers).json()

	def send_message(
			self,
			channel_id: int, 
			text: str, 
			last_received_id: int = 0):
		data = {
		"channel_id": channel_id,
		"last_received_id": last_received_id,
		"text": text
		}
		return requests.post(
			f"{self.api}/api/chat/send",
			data=data,
			headers=self.headers).json()

	def get_equipment(self):
		return requests.get(
			f"{self.api}/api/equipment",
			headers=self.headers).json()

	def get_skills(self):
		return requests.get(
			f"{self.api}/api/skills",
			headers=self.headers).json()

	def get_backpack(self):
		return requests.get(
			f"{self.api}/api/backpack",
			headers=self.headers).json()

	def route_location(self, route_id: int):
		data = {"routeId": route_id}
		return requests.post(
			f"{self.api}/api/location/select-route", 
			data=data, 
			headers=self.headers).json()

	def get_quests_journal(self):
		return requests.get(
			f"{self.api}/api/quest/journal",
			headers=self.headers).json()

	def get_friends(self):
		return requests.get(
			f"{self.api}/api/friends",
			headers=self.headers).json()

	def suggest_friends(self, username: str):
		data = {"u": username}
		return requests.post(
			f"{self.api}/api/friends/suggest",
			data=data,
			headers=self.headers).json()

	def send_friend_request(self, user_id: int):
		data = {"id": user_id}
		return requests.post(
			f"{self.api}/api/friends/invite",
			data=data,
			headers=self.headers).json()

	def cancel_friend_request(self, user_id: int):
		data = {"id": user_id}
		return requests.post(
			f"{self.api}/api/friends/invite/cancel",
			data=data,
			headers=self.headers).json()

	def get_battles_history(self):
		return requests.get(
			f"{self.api}/api/battle/history",
			headers=self.headers).json()

	def start_battle(self, id: str, hp: int, position: int):
		data = {
		"id": id,
		"hp": hp,
		"pos": position
		}
		return requests.post(
			f"{self.api}/api/location/attack", 
			data=data, 
			headers=self.headers).json()

	def attack_monster(self, action_id: int, target_id: int = 0):
		data = {
		"actionId": action_id,
		"targetId": target_id
		}
		return requests.post(
			f"{self.api}/api/battle/current", 
			data=data, 
			headers=self.headers).json()

	def get_current_battle(self):
		return requests.get(
			f"{self.api}/api/battle/current",
			headers=self.headers).json()

	def finish_battle(self):
		return requests.post(
			f"{self.api}/api/battle/finish",
			headers=self.headers).json()

	def pick_up_item(self, item_id: int):
		data = {"itemId": item_id}
		return requests.post(
			f"{self.api}/api/location/pick-up", 
			data=data, 
			headers=self.headers).json()

	def get_monster_info(self, name: str):
		return requests.get(
			f"{self.api}/api/location/monster/{name}", 
			headers=self.headers).json()
