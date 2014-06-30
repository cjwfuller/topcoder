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
			highest = max(j for i, j in enumerate(points) if i not in awarded)
			highest_posns = [i for i, j in enumerate(points) if j == highest]
			for m in highest_posns:
				bonuses[m] += 1
				# ensure people only awarded once for highest, second highest, ...
				awarded.append(m)
				count += 1
				# ensure people only awarded once when there are multiple highest points the same
				if(count > extra):
					break
		return bonuses