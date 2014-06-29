from __future__ import division

class Bonuses:
	def getDivision(self, points):
		bonuses = []
		# calculate bonuses
		total = sum(points)
		extra = 0
		for p in points:
			percent = p / total * 100
			extra += percent % 1
			bonuses.append(int(percent))
		# award any extra points
		extra = round(extra)
		count = 1
		awarded = []
		while count <= extra:
			maximum = max(y for x, y in enumerate(points) if x not in awarded)
			maximums = [i for i, j in enumerate(points) if j == maximum]
			for m in maximums:
				bonuses[m] += 1
				awarded.append(m)
				count += 1
				if(count > extra):
					break
		return bonuses